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
    [SerializeField] SpriteRenderer bubbleBackground;
    [SerializeField] TMPro.TMP_Text question;
    [SerializeField] TMPro.TMP_Text[] options;
    [SerializeField] GameObject optionParent;

    private void OnEnable()
    {
        options = optionParent.GetComponentsInChildren<TMPro.TMP_Text>();
    }

    public void LoadInstanceText(string path) {
        using (StreamReader r = new StreamReader(path))
        {
            string json = r.ReadToEnd();
            content = JsonUtility.FromJson<PreviewContent>(json);
        }
        // TODO: check error
        question.SetText(content.question);
        for (int i = 0; i < options.Length; ++i) {
            options[i].SetText(content.options[i]);
        }
    }

    public void UpdateListTitle(string txt) {
        listTitle.SetText(txt);
    }

    public void UpdateBubbleBackground(Sprite bg) {
        bubbleBackground.sprite = bg;
    }
}
