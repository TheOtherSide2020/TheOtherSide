using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PollingVRTouchPoint : VRTouchPoint
{
    PollingTouchPoint tp;

    protected override void Start()
    {
        tp = gameObject.GetComponent<PollingTouchPoint>();
    }

    // Update is called once per frame
    protected override void Update()
    {
        if (isTouching)
        {
            tp.IncreaseProgress(Time.deltaTime / PollingTouchPointController.Instance.loadingTime);
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
