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
    string[] instanceFolderNames = { "ShowcaseInstance", "SimplePollingInstance", "TextInstance"};
    string instancePath = @"..\TemplateJsonInstance\";
    string instanceEditorPath = @"..\..\TemplateJsonInstance\";

    // preview panel
    string[] contentListTitles = { "Showcase", "Polling System", "Conversation" };
    [SerializeField] Transform contentListParent;
    [SerializeField] GameObject contentListButton;
    [SerializeField] Sprite[] bubbleBackgrounds;
    
    private void Start()
    {
        BacktoTemplateSelection();
        instanceList = new string[(SceneLoader.Instance.GetNumberOfTemplate())];

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
            PreviewContent(0);
        }
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
        ContentListButton[] existedButtons = contentListParent.GetComponentsInChildren<ContentListButton>();
        foreach (ContentListButton b in existedButtons) {
            Destroy(b.gameObject);
        }

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
        }
    }

    public void EnterPreview(int idx) {
        // update active template
        currentTemplate = idx;
        // load list of instance names
        // TODO: change to list of list
        UpdateContentList();
        GenerateContentListButtons();
        PreviewPanel.Instance.UpdateBubbleBackground(bubbleBackgrounds[currentTemplate]);
        PreviewPanel.Instance.UpdateListTitle(contentListTitles[currentTemplate] + " Content List");
        // set active
        panels[1].SetActive(true);
        panels[0].SetActive(false);
    }

    // back button onclick
    public void BacktoTemplateSelection() {
        panels[0].SetActive(true);
        panels[1].SetActive(false);
    }

    // after clicking on preview instance
    public void PreviewContent(int idx) {
        currentPreviewInstancePath = instanceList[idx];
        // load instance content
        PreviewPanel.Instance.LoadInstanceText(currentPreviewInstancePath);
    }

    // click display button
    public void DisplayInstance(string name) {
        // update file name
        // load scene
        SceneLoader.Instance.LoadScene(currentTemplate);
    }

    public string GetCurrentPreviewPath() {
        return currentPreviewInstancePath;
    }
}
