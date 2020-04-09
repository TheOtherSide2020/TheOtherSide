using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class TextTemplateTouchPoint : TouchPoint
{
    [SerializeField] ContainerSizeUpdater sizeUpdater;
    public void AdjustContainer()
    {
        sizeUpdater.UpdateSize();
    }

    public void ResetCheckMark()
    {
        textDisplay.gameObject.SetActive(true);
        checkMarkImage.fillAmount = 0f;
    }

    public void ShowCheckMark()
    {
        textDisplay.gameObject.SetActive(false);
        StartCoroutine(FillCheckMark(TouchPointController.Instance.checkMarkFillingTime));
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
