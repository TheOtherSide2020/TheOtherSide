using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PreviewContentLoader : MonoBehaviour
{
    [SerializeField] TMPro.TMP_Text[] contents;

    private void OnEnable()
    {
        contents = GetComponentsInChildren<TMPro.TMP_Text>();
    }

    public void SetPreviewContent(string question, string[] options) {
        contents[0].SetText(question);
        for (int i = 0; i < options.Length; ++i)
        {
            contents[i+1].SetText(options[i]);
        }
    }
}
