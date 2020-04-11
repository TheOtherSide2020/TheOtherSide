using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class TextTemplateTouchPoint : TouchPoint
{
    [SerializeField] Image checkMarkImage;

    override public void StopProgress() {
        if (!interactionEnabled) return;
        if (progress >= 1f)
        {
            return;
        }
        TextTemplateTouchPointController.Instance.OnAbortTouch(id);
    }

    override public void IncreaseProgress(float amount) {
        if (!interactionEnabled) return;
        if (progress == 0f)
        {
            TextTemplateTouchPointController.Instance.OnStartTouch(id);
        }
        base.IncreaseProgress(amount);
    }

    override protected void OnEndVoting()
    {
        TextTemplateTouchPointController.Instance.OnEndTouch(id);
    }

    public void ResetCheckMark()
    {
        textDisplay.gameObject.SetActive(true);
        checkMarkImage.fillAmount = 0f;
    }

    public void ShowCheckMark()
    {
        textDisplay.gameObject.SetActive(false);
        StartCoroutine(FillCheckMark(TextTemplateTouchPointController.Instance.checkMarkFillingTime));
    }

    IEnumerator FillCheckMark(float finishTimeInSec)
    {
        while (checkMarkImage.fillAmount < 1f)
        {
            checkMarkImage.fillAmount += Time.deltaTime / finishTimeInSec;
            yield return new WaitForEndOfFrame();
        }
    }
}
