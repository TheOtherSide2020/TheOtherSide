using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class VRTouchPoint : MonoBehaviour
{
    //TouchPoint tp;
    protected bool isTouching = false;

    protected virtual void Start()
    {
        //tp = gameObject.GetComponent<TouchPoint>();
    }

    // Update is called once per frame
    protected virtual void Update()
    {
        //if (isTouching) {
        //    tp.IncreaseProgress(Time.deltaTime / TouchPointController.Instance.loadingTime); 
        //}
    }

    // Called by 2D Mouse Click
    public void OnPointerDown() {
        if (!isTouching) {
            isTouching = true;
        }
    }

    public virtual void OnPointerUp() {
        //tp.StopProgress();
        isTouching = false;
    }

    // Called by VR hand touch
    protected virtual void OnTriggerEnter(Collider other)
    {
        if (other.gameObject.CompareTag("Hand")) {
            isTouching = true;
        }
    }

    protected virtual void OnTriggerExit(Collider other)
    {
        if (other.gameObject.CompareTag("Hand"))
        {
            //tp.StopProgress();
            isTouching = false;
        }
    }
}
