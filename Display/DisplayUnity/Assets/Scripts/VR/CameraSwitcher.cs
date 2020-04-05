using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CameraSwitcher : MonoBehaviour
{
    Camera Camera2D;
    string defaultKeycode = "alpha";
    [SerializeField] int defaultDisplay;
    [SerializeField] Camera[] VRCameras;
    void Start()
    {
        Camera2D = GetComponent<Camera>();
        defaultKeycode = defaultDisplay.ToString();
    }

    // Update is called once per frame
    void Update()
    {
        if (Input.GetKeyDown(KeyCode.Alpha1))
        {
            // in 2D
            Camera2D.targetDisplay = 0;
            foreach (Camera c in VRCameras)
            {
                c.targetDisplay = 5;
            }
        }
        //if (Input.GetKeyDown(defaultKeycode))
        //{
        //    if (Camera2D.targetDisplay == 0)
        //    {
        //        // switch to original display
        //        //Camera2D.targetDisplay = 5;
        //        Debug.Log("Switch camera " + defaultDisplay + " back");
        //        //foreach (Camera c in VRCameras) {
        //        //    c.targetDisplay = 0;
        //        //}
        //        Camera2D.targetDisplay = defaultDisplay - 1;
        //    }
        //    else {
        //        //foreach (Camera c in VRCameras)
        //        //{
        //        //    c.targetDisplay = 5;
        //        //}
        //        Camera2D.targetDisplay = 0;
        //        //foreach (Camera c in VRCameras)
        //        //{
        //        //    c.targetDisplay = defaultDisplay - 1;
        //        //}
        //        Debug.Log("Switch camera " + defaultDisplay + " to Display 1");
        //    }
        //}
    }
}
