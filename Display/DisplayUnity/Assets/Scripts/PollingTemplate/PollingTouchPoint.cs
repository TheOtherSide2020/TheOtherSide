using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class PollingTouchPoint : TouchPoint
{
    //[SerializeField] ContainerSizeUpdater sizeUpdater;
    [SerializeField] TMPro.TMP_Text countText;

    protected override void Start()
    {
        base.Start();
    }


    override public void StopProgress()
    {
        if (!interactionEnabled) return;
        if (progress >= 1f)
        {
            return;
        }
        PollingTouchPointController.Instance.OnAbortTouch(id);
    }

    override public void IncreaseProgress(float amount)
    {
        if (!interactionEnabled) return;
        if (progress == 0f)
        {
            PollingTouchPointController.Instance.OnStartTouch(id);
        }
        base.IncreaseProgress(amount);
    }

    override protected void OnEndVoting()
    {
        PollingTouchPointController.Instance.OnEndTouch(id);
    }


    public void SetResultText(string txt) {
        countText.SetText(txt);
    }
}
