using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class MainBubbleSingleMessage : MonoBehaviour
{
    TMPro.TextMeshPro textDisplay;

    void Awake()
    {
        textDisplay = GetComponentInChildren<TMPro.TextMeshPro>();
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    public void SetText(string txt) {
        textDisplay.SetText(txt);
    }
}
