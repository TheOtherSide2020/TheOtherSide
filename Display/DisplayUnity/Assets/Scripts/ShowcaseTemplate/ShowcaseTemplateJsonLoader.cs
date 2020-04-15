using System;
using System.Collections;
using System.Collections.Generic;
using System.IO;
using UnityEngine;

public class ShowcaseTemplateJsonLoader : MonoBehaviour
{
    public static ShowcaseTemplateJsonLoader Instance = null;

    [Serializable]
    public class ShowcaseContent
    {
        public string question;
        public string videoPath;
        public string picturePath;
        public string[] options;
    }

    ShowcaseContent loadContent;
    [SerializeField] bool usingHardCode = false;
    [SerializeField] string path;
    [SerializeField] Sprite pictureSprite;
    private void Awake()
    {
        if (Instance == null)
        {
            Instance = this;
        }
        if (usingHardCode)
        {
            loadContent = new ShowcaseContent();
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
            using (StreamReader r = new StreamReader("playtest.json"))
            {
                string json = r.ReadToEnd();
                loadContent = JsonUtility.FromJson<ShowcaseContent>(json);
            }
            LoadSprite(loadContent.picturePath);
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

    public bool UseVideo() {
        return false;
    }

    public string GetVideoUrl()
    {
        return loadContent.videoPath;
    }

    public string GetPictureUrl()
    {
        return loadContent.picturePath;
    }

    public Sprite GetPicture() {
        return pictureSprite;
    }

    void LoadSprite(string path, float pixelsPerUnit = 100.0f)
    {
        // Load a PNG or JPG image from disk to a Texture2D
        Texture2D spriteTexture = LoadTexture(path);
        pictureSprite = Sprite.Create(
            spriteTexture, 
            new Rect(0, 0, spriteTexture.width, spriteTexture.height), 
            new Vector2(0, 0), pixelsPerUnit);
    }

    public Texture2D LoadTexture(string path)
    {

        // Load a PNG or JPG file from disk to a Texture2D
        // Returns null if load fails

        Texture2D Tex2D;
        byte[] FileData;

        if (File.Exists(path))
        {
            FileData = File.ReadAllBytes(path);
            Tex2D = new Texture2D(2, 2);           // Create new "empty" texture
            if (Tex2D.LoadImage(FileData))           // Load the imagedata into the texture (size is set automatically)
                return Tex2D;                 // If data = readable -> return texture
        }
        return null;                     // Return null if load failed
    }
}

