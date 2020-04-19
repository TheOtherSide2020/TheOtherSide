using System.Collections;
using System.Collections.Generic;
using System.IO;
using UnityEngine;
using UnityEngine.UI;

public class SelectionMenu : MonoBehaviour
{
    #region Singleton
    public static SelectionMenu Instance = null;

    private void Awake()
    {
        if (Instance == null)
        {
            Instance = this;
        }
    }
    #endregion

    class DisplayingInstance
    {
        public int templateIdx;
        public int instanceIdx;
        public string instanceName;
        public DisplayingInstance(int tidx, int iidx, string iname) {
            templateIdx = tidx;
            instanceIdx = iidx;
            instanceName = iname;
        }
    }
    // (template idx, instance name) 
    [SerializeField] DisplayingInstance currentDisplayInstance = null;

    [SerializeField] GameObject[] panels;
    [SerializeField] int currentTemplate = -1;
    [SerializeField] string[] instanceList;
    [SerializeField] string currentPreviewInstancePath;
    
    string[] instanceFolderNames = { "ShowcaseInstance", "SimplePollingInstance", "TextInstance"};
    string instancePath = @"..\TemplateJsonInstance\";
    string instanceEditorPath = @"..\..\TemplateJsonInstance\";

    // preview panel
    string[] contentListTitles = { "Showcase", "Polling System", "Conversation" };
    [SerializeField] int currentPreviewInstance = -1;
    [SerializeField] Transform contentListParent;
    [SerializeField] List<ContentListButton> contentListButtons;
    [SerializeField] GameObject contentListButton;
    [SerializeField] Sprite[] bubbleBackgrounds;
    [SerializeField] Button displayButton;

    // result writer
    string resultPath = @"..\ResultData\";
    string resultEditorPath = @"..\..\ResultData\";
    string[] resultFolderNames = { "Showcase\\", "Polling\\", "Text\\" };
    [SerializeField] string currentPreviewResultPath;

    private void Start()
    {
        BacktoTemplateSelection();
        instanceList = new string[(SceneLoader.Instance.GetNumberOfTemplate())];
        contentListButtons = new List<ContentListButton>();
        displayButton.interactable = false;
        // debug
        //currentTemplate = 0;
        //UpdateContentList();
        //GenerateContentListButtons();
    }

    private void Update()
    {
        if (Input.GetKeyDown(KeyCode.F1)) {
            EnterPreview(0);
        }
        if (Input.GetKeyDown(KeyCode.F2))
        {
            EnterPreview(1);
        }
        if (Input.GetKeyDown(KeyCode.F3))
        {
            PreviewContent(0, "test");
        }
        if (Input.GetKeyDown(KeyCode.F6))
        {
            PreviewContent(1, "test");
        }
        if (Input.GetKeyDown(KeyCode.F4))
        {
            DisplayInstance("");
        }
        if (Input.GetKeyDown(KeyCode.F5))
        {
            RefreshContentList();
        }
    }

    // refresh button
    public void RefreshContentList() {
        PreviewPanel.Instance.ClearPreviewInstanceText(currentTemplate);
        currentPreviewInstance = -1;
        displayButton.interactable = false;
        UpdateContentList();
        GenerateContentListButtons();
    }

    public void UpdateContentList() {
        // load and save
        string fileName = instancePath + instanceFolderNames[currentTemplate];
#if UNITY_EDITOR
        fileName = instanceEditorPath + instanceFolderNames[currentTemplate];
#endif
        instanceList = Directory.GetFiles(fileName, "*.json", SearchOption.TopDirectoryOnly);
    }

    public void GenerateContentListButtons() {
        // TODO: Object pool
        foreach (ContentListButton b in contentListButtons) {
            Destroy(b.gameObject);
        }
        contentListButtons = new List<ContentListButton>();

        // create new buttons
        int len = instanceList.Length;
        for (int i = 0; i < len; ++i) {
            // get short file name: *.json
            string path = instanceList[i];
            char[] delimiterChars = { '.', '\\' };
            string[] parts = path.Split(delimiterChars);
            GameObject newButton = Instantiate(contentListButton, contentListParent);
            ContentListButton contentButton = newButton.GetComponent<ContentListButton>();
            contentButton.idx = i;
            contentButton.title = (parts[parts.Length - 2]);
            contentButton.UpdateTitle();
            contentButton.SetActiveDisplayStatus(false);
            contentListButtons.Add(contentButton);
        }

        // check if cuurent display instance still exists
        if (currentDisplayInstance != null && currentTemplate == currentDisplayInstance.templateIdx)
        {
            string activeName = currentDisplayInstance.instanceName;
            for (int i = 0; i < len; ++i)
            {
                // update green dot if found matching instance
                ContentListButton button = contentListButtons[i];
                if (activeName.Equals(button.title)) {
                    currentDisplayInstance.instanceIdx = i;
                    button.SetActiveDisplayStatus(true);
                    return;
                }
            }
            // reset if no matching instance found
            currentDisplayInstance = null;
        }
    }

    // click on template button, enter preview panel
    public void EnterPreview(int idx) {
        // update active template
        currentTemplate = idx;
        // load list of instance names
        // TODO: change to list of list
        UpdateContentList();
        GenerateContentListButtons();
        // update UI text and background
        PreviewPanel.Instance.UpdatePreviewUI(
            currentTemplate,
            bubbleBackgrounds[currentTemplate], 
            contentListTitles[currentTemplate] + " Content List");
        // set active
        panels[1].SetActive(true);
        panels[0].SetActive(false);
    }

    // back button onclick
    public void BacktoTemplateSelection() {
        // clear UI text
        PreviewPanel.Instance.ClearUIText(currentTemplate);
        currentPreviewInstance = -1;
        displayButton.interactable = false;
        panels[0].SetActive(true);
        panels[1].SetActive(false);
    }

    // after clicking on preview instance
    public void PreviewContent(int idx, string shortTitle) {
        currentPreviewInstancePath = instanceList[idx];
        currentPreviewInstance = idx;
        displayButton.interactable = true;
        // load instance content
        PreviewPanel.Instance.LoadInstanceText(currentPreviewInstancePath, currentTemplate, shortTitle);
    }

    // click display button
    public void DisplayInstance(string name) {
        if (currentPreviewInstance == -1) return;
        // update green active dot
        if (currentDisplayInstance != null && currentTemplate == currentDisplayInstance.templateIdx) {
            contentListButtons[currentDisplayInstance.instanceIdx].SetActiveDisplayStatus(false);
        }
        Debug.Log("display: " + currentPreviewInstance);
        contentListButtons[currentPreviewInstance].SetActiveDisplayStatus(true);
        currentDisplayInstance = new DisplayingInstance(currentTemplate, currentPreviewInstance, contentListButtons[currentPreviewInstance].title);
        SetCurrentResultPath(currentDisplayInstance.instanceName);
        // load scene
        SceneLoader.Instance.LoadScene(currentTemplate);
    }

    public string GetCurrentPreviewPath() {
        return currentPreviewInstancePath;
    }

    public string GetCurrentResultPath()
    {
        return currentPreviewResultPath;
    }

    void SetCurrentResultPath(string title)
    {
        // load and save
        string folderName = resultPath + resultFolderNames[currentTemplate];
#if UNITY_EDITOR
        folderName = resultEditorPath + resultFolderNames[currentTemplate];
#endif
        currentPreviewResultPath = folderName + title + ".json";
    }
}
