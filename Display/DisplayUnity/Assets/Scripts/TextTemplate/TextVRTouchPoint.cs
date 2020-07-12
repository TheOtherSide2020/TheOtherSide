using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class TextVRTouchPoint : VRTouchPoint
{
    TextTemplateTouchPoint tp;

    protected override void Start()
    {
        tp = gameObject.GetComponent<TextTemplateTouchPoint>();
    }

    // Update is called once per frame
    protected override void Update()
    {
        // update touch point progress per frame if touching
        if (isTouching)
        {
            tp.IncreaseProgress(Time.deltaTime / TextTemplateTouchPointController.Instance.loadingTime);
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
