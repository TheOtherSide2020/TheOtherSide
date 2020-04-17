using System.Collections;
using System.Collections.Generic;
using System.IO;
using UnityEngine;

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

    [SerializeField] GameObject[] panels;
    [SerializeField] int currentTemplate = -1;
    [SerializeField] string[] instanceList;
    [SerializeField] string currentPreviewInstancePath;
    [SerializeField] string[] instanceFolderNames;
    string instancePath = @"..\TemplateJsonInstance\SimplePollingInstance\";
    string instanceEditorPath = @"..\..\TemplateJsonInstance\SimplePollingInstance\";

    // preview panel
    [SerializeField] Transform contentListParent;
    [SerializeField] GameObject contentListButton;

    private void Start()
    {
        panels[0].SetActive(true);
        panels[1].SetActive(false);
        instanceList = new string[(SceneLoader.Instance.GetNumberOfTemplate())];
        UpdateContentList();
    }

    public void UpdateContentList() {
        // load and save
        string fileName = instancePath;
#if UNITY_EDITOR
        fileName = instanceEditorPath;
#endif
        instanceList = Directory.GetFiles(fileName, "*.json", SearchOption.TopDirectoryOnly);
        // spilt file name
    }

    public void EnterPreview(int idx) {
        panels[1].SetActive(true);
        panels[0].SetActive(false);

        // load list of instance names
        // TODO: change to list of list
        if (instanceList == null) {
            UpdateContentList();
        }
        // set preview content in preview panel
        currentTemplate = idx;    
    }

    public void BacktoTemplateSelection() {
        panels[0].SetActive(true);
        panels[1].SetActive(false);
    }

    // after clicking on preview instance
    public void PreviewContent(int idx) {
        currentPreviewInstancePath = instanceList[idx];
    }

    public void DisplayInstance(string name) {
        // update file name
        // load scene
        SceneLoader.Instance.LoadScene(currentTemplate);
    }

    public string GetCurrentPreviewPath() {
        return currentPreviewInstancePath;
    }
}
