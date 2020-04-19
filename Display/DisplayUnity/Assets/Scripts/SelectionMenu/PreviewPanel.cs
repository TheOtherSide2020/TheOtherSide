using System;
using System.Collections;
using System.Collections.Generic;
using System.IO;
using UnityEngine;

public class PreviewPanel : MonoBehaviour
{
    #region Singleton
    public static PreviewPanel Instance = null;

    private void Awake()
    {
        if (Instance == null)
        {
            Instance = this;
        }
        contentLoaders = GetComponentsInChildren<PreviewContentLoader>();
    }
    #endregion

    [Serializable]
    public class PreviewContent
    {
        public string question;
        public string[] options;
    }

    PreviewContent content;

    [SerializeField] TMPro.TMP_Text listTitle;
    [SerializeField] TMPro.TMP_Text instanceTitle;
    [SerializeField] SpriteRenderer bubbleBackground;
    [SerializeField] PreviewContentLoader[] contentLoaders;

    public void LoadInstanceText(string path, int templateIdx, string title) {
        // read instance from json file
        using (StreamReader r = new StreamReader(path))
        {
            string json = r.ReadToEnd();
            content = JsonUtility.FromJson<PreviewContent>(json);
        }
        // TODO: check error
        
        // set text in preview content
        contentLoaders[templateIdx].SetPreviewContent(content.question, content.options);

        // set short instance title
        instanceTitle.SetText(title);
    }

    public void ClearUIText(int templateIdx) {
        UpdateListTitle("");
        instanceTitle.SetText("");
        contentLoaders[templateIdx].SetPreviewContent("", new string[4]);
    }

    public void ClearPreviewInstanceText(int templateIdx) {
        instanceTitle.SetText("");
        contentLoaders[templateIdx].SetPreviewContent("", new string[4]);
    }

    void UpdateListTitle(string txt) {
        listTitle.SetText(txt);
    }

    void UpdateBubbleBackground(Sprite bg) {
        bubbleBackground.sprite = bg;
    }

    public void UpdatePreviewUI(int templateIdx, Sprite bg, string listTitle) {
        // enable certain template preview content
        for (int i = 0; i < contentLoaders.Length; ++i)
        {
            if (i == templateIdx)
            {
                contentLoaders[i].gameObject.SetActive(true);
            }
            else
            {
                contentLoaders[i].gameObject.SetActive(false);
            }
        }

        // update background
        UpdateBubbleBackground(bg);
        UpdateListTitle(listTitle);
    }
}
