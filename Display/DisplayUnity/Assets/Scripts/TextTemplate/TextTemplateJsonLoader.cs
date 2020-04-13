using System;
using System.Collections;
using System.Collections.Generic;
using System.IO;
using UnityEngine;

public class TextTemplateJsonLoader : MonoBehaviour
{
    public static TextTemplateJsonLoader Instance = null;

    [Serializable]
    public class Content
    {
        public string question;
        public string[] options;
    }

    Content loadContent;
    [SerializeField] bool usingHardCode = false;
    [SerializeField] string path;
    private void Awake()
    {
        if (Instance == null)
        {
            Instance = this;
        }
        if (usingHardCode)
        {
            loadContent = new Content();
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
            using (StreamReader r = new StreamReader(path))
            {
                string json = r.ReadToEnd();
                loadContent = JsonUtility.FromJson<Content>(json);
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
