﻿using System;
using System.Collections;
using System.Collections.Generic;
using System.IO;
using UnityEngine;

public class PollingTemplateJsonLoader : MonoBehaviour
{
    public static PollingTemplateJsonLoader Instance = null;

    [Serializable]
    public class PollingContent
    {
        public string question;
        public string[] options;
    }

    [SerializeField] PollingContent loadContent;
    [SerializeField] bool usingHardCode = false;

    private void Awake()
    {
        if (Instance == null)
        {
            Instance = this;
        }
        if (usingHardCode)
        {
            loadContent = new PollingContent();
            loadContent.options = new string[] {
                "Just try to avoid them.",
                "Let them know how you feel.",
                "It’ll pass, you’ll grow out of it.",
                "I understand, I get that sometimes, too."
            };
            loadContent.question = "The way this person talks to me really makes me uncomfortable, tho I know it’s not intentional. What can I do about it?";
        }
        else
        {
            
            using (StreamReader r = new StreamReader(SelectionMenu.Instance.GetCurrentPreviewPath()))
            {
                string json = r.ReadToEnd();
                loadContent = JsonUtility.FromJson<PollingContent>(json);
            }
        }
        Debug.Log(loadContent);
    }

    public string GetOption(int idx)
    {
        if (idx >= loadContent.options.Length) return "Invalid";
        return loadContent.options[idx];
    }

    public string GetQuestion()
    {
        return loadContent.question;
    }


}
