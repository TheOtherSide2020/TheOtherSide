using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ShowcaseVRTouchPoint : VRTouchPoint
{
    ShowcaseTouchPoint tp;

    protected override void Start()
    {
        tp = gameObject.GetComponent<ShowcaseTouchPoint>();
    }

    // Update is called once per frame
    protected override void Update()
    {
        if (isTouching)
        {
            tp.IncreaseProgress(Time.deltaTime / ShowcaseTouchPointController.Instance.loadingTime);
        }
    }

    public override void OnPointerUp()
    {
        tp.StopProgress();
        isTouching = false;
    }

    protected override void OnTriggerExit(Collider other)
    {
        if (other.gameObject.CompareTag("Hand"))
        {
            tp.StopProgress();
            isTouching = false;
        }
    }
}
