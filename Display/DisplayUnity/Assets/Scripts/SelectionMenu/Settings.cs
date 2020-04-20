using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Settings : MonoBehaviour
{
    // Start is called before the first frame update
    void Awake()
    {
        Screen.SetResolution(1920, 1080, false);
    }

    // Update is called once per frame
    void Update()
    {
        if (Input.GetKeyDown(KeyCode.Escape)) {
            Application.Quit();
        }
        if (Input.GetKeyDown(KeyCode.W))
        {
            Screen.fullScreen = !Screen.fullScreen;
        }
    }
}
