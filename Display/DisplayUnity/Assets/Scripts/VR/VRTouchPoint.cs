using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class VRTouchPoint : MonoBehaviour
{
    TouchPoint tp;
    bool isTouching = false;
    void Start()
    {
        tp = gameObject.GetComponent<TouchPoint>();
    }

    // Update is called once per frame
    void Update()
    {
        if (isTouching) {
            tp.IncreaseProgress(Time.deltaTime / TouchPointController.Instance.loadingTime); 
        }
    }

    public void OnPointerDown() {
        if (!isTouching) {
            isTouching = true;
        }
    }

    public void OnPointerUp() {
        tp.StopProgress();
        isTouching = false;
    }

    private void OnTriggerEnter(Collider other)
    {
        if (other.gameObject.CompareTag("Hand")) {
            isTouching = true;
        }
    }

    //private void OnTriggerStay(Collider other)
    //{
    //    if (other.gameObject.CompareTag("Hand"))
    //    {

    //    }
    //}

    private void OnTriggerExit(Collider other)
    {
        if (other.gameObject.CompareTag("Hand"))
        {
            tp.StopProgress();
            isTouching = false;
        }
    }
}
