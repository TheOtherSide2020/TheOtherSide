using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class ShowcaseTouchPoint : TouchPoint
{
    //[SerializeField] ContainerSizeUpdater sizeUpdater;

    override public void StopProgress()
    {
        if (!interactionEnabled) return;
        if (progress >= 1f)
        {
            return;
        }
        ShowcaseTouchPointController.Instance.OnAbortTouch(id);
    }

    override public void IncreaseProgress(float amount)
    {
        if (progress == 0f)
        {
            ShowcaseTouchPointController.Instance.OnStartTouch(id);
        }
        base.IncreaseProgress(amount);
    }

    override protected void OnEndVoting()
    {
        ShowcaseTouchPointController.Instance.OnEndTouch(id);
    }
}
