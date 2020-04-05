using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.IO;
using System;

public class JsonLoader : MonoBehaviour
{
    public static JsonLoader Instance = null;

    [Serializable]
    public class Content
    {
        public string question;
        public string[] options;
    }

    Content loadContent;
    private void Awake()
    {
        if (Instance == null)
        {
            Instance = this;
        }
        using (StreamReader r = new StreamReader("playtest.json")) {
            string json = r.ReadToEnd();
            loadContent = JsonUtility.FromJson<Content>(json);
        } 
        Debug.Log(loadContent);
    }

    public string GetOption(int idx) {
        if (idx >= loadContent.options.Length) return "Invaild";
        return loadContent.options[idx];
    }

    public string GetQuestion() {
        return loadContent.question;
    }
}
