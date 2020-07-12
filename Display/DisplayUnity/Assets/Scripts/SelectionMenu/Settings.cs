using System;
using System.Collections;
using System.Collections.Generic;
using System.IO;
using UnityEngine;

public class Settings : MonoBehaviour
{
    [SerializeField] GameObject settingsPanel;
    [SerializeField] float offsetMultiplier = 0.1f;
    [SerializeField] TMPro.TMP_InputField lightThreshold;
    [SerializeField] TMPro.TMP_Dropdown numberSensorsDropdown;
    [SerializeField] GameObject portDropdownParent;
    [SerializeField] TMPro.TMP_Dropdown[] portDropdowns;
    [SerializeField] GameObject projectorOffsetParent;
    [SerializeField] TMPro.TMP_InputField[] projectOffsetInput;
    [SerializeField] Transform projectorCamera;
    [SerializeField] Vector3 originalCameraPos;

    [SerializeField] SavedSettings loadedSettings, currentSettings;

    Dictionary<string, Vector3> offsetMap = new Dictionary<string, Vector3>() {
        { "x", new Vector3(1f, 0, 0)},
        { "y", new Vector3(0, 1f, 0)},
        { "z", new Vector3(0, 0, 1f)}
    };

    [Serializable]
    class Offset {
        public float X;
        public float Y;               
        public float Z;
    }

    [Serializable]
    class SavedSettings { 
        public float sensibilityThreshold;
        public int maxNumberOfSensors;
        public int numberOfSensors;
        public int[] ports;
        public Offset projectorOffset;
    }

    string settingPath = @".\Settings.json";
    string settingEditorPath = @"..\..\DisplayBuild\Settings.json";

    void Awake()
    {
        // set screen
        Screen.SetResolution(1920, 1080, false);
       
        // read settings from json
        string path = settingPath;
#if UNITY_EDITOR
        path = settingEditorPath;
#endif
        if (File.Exists(path))
        {
            using (StreamReader r = new StreamReader(path))
            {
                string json = r.ReadToEnd();
                loadedSettings = JsonUtility.FromJson<SavedSettings>(json);
                currentSettings = JsonUtility.FromJson<SavedSettings>(json);
            }
        }

        // set dropdown options
        List<TMPro.TMP_Dropdown.OptionData> options = new List<TMPro.TMP_Dropdown.OptionData>();
        for (int i = 1; i <= loadedSettings.maxNumberOfSensors; ++i) {
            TMPro.TMP_Dropdown.OptionData option = new TMPro.TMP_Dropdown.OptionData(i.ToString());
            options.Add(option);
        }
        numberSensorsDropdown.AddOptions(options);
        portDropdowns = portDropdownParent.GetComponentsInChildren<TMPro.TMP_Dropdown>();
        // TODO: auto add options

        // get input fields
        projectOffsetInput = projectorOffsetParent.GetComponentsInChildren<TMPro.TMP_InputField>();

        // camera
        originalCameraPos = projectorCamera.position;
    }

    private void Start()
    {
        LoadSettings();
        SetPortSettings();
        SetPanelStatus(false);
    }

    // Update is called once per frame
    void Update()
    {
        if (Input.GetKeyDown(KeyCode.Escape)) {
            Application.Quit();
        }
        if (Input.GetKeyDown(KeyCode.W))
        {
            Screen.fullScreen = !Screen.fullScreen;
        }
    }

    public void SetPanelStatus(bool isActive) {
        settingsPanel.SetActive(isActive);
    }

    void SetPortSettings() {
        if (PhidgetsInputManager.Instance)
        {
            PhidgetsInputManager.Instance.SetSensorPorts(
                currentSettings.numberOfSensors,
                currentSettings.ports);
        }
    }

    public void SaveSettings() {
        // set sensor ports
        SetPortSettings();
        // copy current settings to loaded
        string json = JsonUtility.ToJson(currentSettings);
        loadedSettings = JsonUtility.FromJson<SavedSettings>(json);
        // write new settings to file
        string path = settingPath;
#if UNITY_EDITOR
        path = settingEditorPath;
#endif
        File.WriteAllText(path, json);
    }

    // Called when the cancel button is clicked
    public void CancelSettings() {
        // reset back to previous saved settings
        LoadSettings();
        // reset camera position to the saved one
        projectorCamera.position = originalCameraPos + new Vector3(
            loadedSettings.projectorOffset.X,
            loadedSettings.projectorOffset.Y,
            loadedSettings.projectorOffset.Z);
    }

    public void LoadSettings() {
        // set threshold
        lightThreshold.SetTextWithoutNotify(loadedSettings.sensibilityThreshold.ToString()) ;
        OnChangeLightThreshold();

        // set sensor ports
        numberSensorsDropdown.value = loadedSettings.numberOfSensors - 1;
        OnChangeNumberOfSensors();
        for (int i = 1; i <= loadedSettings.numberOfSensors; ++i)
        {
            // set active sensor
            portDropdowns[i - 1].value = loadedSettings.ports[i-1];
        }

        // set projector offset
        InitilizeProjectorOffsetDisplay();
        projectorCamera.position += new Vector3(
            loadedSettings.projectorOffset.X,
            loadedSettings.projectorOffset.Y,
            loadedSettings.projectorOffset.Z);
    }

    public void OnChangeLightThreshold() {
        currentSettings.sensibilityThreshold = float.Parse(lightThreshold.text);
        // change in phidgets input manager
        if (PhidgetsInputManager.Instance) {
            PhidgetsInputManager.Instance.SetSensorThreshold(currentSettings.sensibilityThreshold);
        }
    }

    public void OnChangeNumberOfSensors()
    {
        int newNum = numberSensorsDropdown.value + 1;
        // set new ports
        int[] newPorts = new int[newNum];
        for (int i = 0; i < newNum; ++i) {
            if (i < currentSettings.ports.Length)
            {
                newPorts[i] = currentSettings.ports[i];
            }
            else {
                newPorts[i] = i;
            }
        }
        currentSettings.ports = newPorts;
        currentSettings.numberOfSensors = newNum;
        for (int i = 1; i <= loadedSettings.maxNumberOfSensors; ++i)
        {
            // set active sensor
            portDropdowns[i - 1].interactable = i <= newNum;
        }
    }

    public void OnChangePort(int id) {
        // port switch
        currentSettings.ports[id] = portDropdowns[id].value;
    }

    public void InitilizeProjectorOffsetDisplay()
    {
        projectOffsetInput[0].SetTextWithoutNotify(loadedSettings.projectorOffset.X.ToString());
        projectOffsetInput[1].SetTextWithoutNotify(loadedSettings.projectorOffset.Y.ToString());
        projectOffsetInput[2].SetTextWithoutNotify(loadedSettings.projectorOffset.Z.ToString());
    }

    public void SetProjectOffsetDisplay() {
        projectOffsetInput[0].SetTextWithoutNotify(currentSettings.projectorOffset.X.ToString());
        projectOffsetInput[1].SetTextWithoutNotify(currentSettings.projectorOffset.Y.ToString());
        projectOffsetInput[2].SetTextWithoutNotify(currentSettings.projectorOffset.Z.ToString());
    }

    public void OnOffsetChangeLeft(string axis) {
        Vector3 offsetChange = -offsetMultiplier * offsetMap[axis];
        // set camera
        projectorCamera.position += offsetChange;
        currentSettings.projectorOffset.X += offsetChange.x;
        currentSettings.projectorOffset.Y += offsetChange.y;
        currentSettings.projectorOffset.Z += offsetChange.z;
        SetProjectOffsetDisplay();
    }

    public void OnOffsetChangeRight(string axis)
    {
        Vector3 offsetChange = offsetMultiplier * offsetMap[axis];
        // set camera
        projectorCamera.position += offsetChange;
        currentSettings.projectorOffset.X += offsetChange.x;
        currentSettings.projectorOffset.Y += offsetChange.y;
        currentSettings.projectorOffset.Z += offsetChange.z;
        SetProjectOffsetDisplay();
    }

    public void OnOffsetChange()
    {
        // edit input field
        Vector3 offset = new Vector3(
            float.Parse(projectOffsetInput[0].text),
            float.Parse(projectOffsetInput[1].text),
            float.Parse(projectOffsetInput[2].text));
        projectorCamera.position = originalCameraPos + offset;
        currentSettings.projectorOffset.X = offset.x;
        currentSettings.projectorOffset.Y = offset.y;
        currentSettings.projectorOffset.Z = offset.z;
    }

    private void OnDestroy()
    {
        
    }
}
