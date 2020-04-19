using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class WaterUpdater : MonoBehaviour
{
    [SerializeField] RectTransform[] waterComponents;
    [SerializeField] float increaseAmount = 0f;
    [SerializeField] float increaseAmountPerSec;
    [SerializeField] float resetAmountPerSec;
    public float waterResetTime = 2f;

    public void UpdateIncreaseAmount(int votes) {
        Vector2 perUnit = (waterComponents[2].anchoredPosition - waterComponents[1].anchoredPosition) / votes;
        increaseAmount = perUnit.y;
        increaseAmountPerSec = increaseAmount / ShowcaseTouchPointController.Instance.waterIncreaseTime;
        resetAmountPerSec = 
            (waterComponents[1].anchoredPosition - waterComponents[2].anchoredPosition).y / waterResetTime;
    }

    // set water level (no animation
    public void SetWaterLevel(int unit) {
        waterComponents[0].anchoredPosition =
            waterComponents[1].anchoredPosition +
            unit * new Vector2(0, increaseAmount);
    }

    public void IncreaseWaterLevel(bool reset = false, int unit = 1) {
        StartCoroutine(
            IncreaseWaterAnimation(reset, 
                waterComponents[0].anchoredPosition.y + unit * increaseAmount));
    }

    public void ResetWaterLevel() {
        StartCoroutine(
            DecreaseWaterAnimation(waterComponents[1].anchoredPosition.y));
    }

    IEnumerator IncreaseWaterAnimation(bool reset, float aimingY) {
        while (waterComponents[0].anchoredPosition.y < aimingY) {
            yield return new WaitForEndOfFrame();
            waterComponents[0].anchoredPosition +=
                new Vector2(0, Time.deltaTime * increaseAmountPerSec);
            //Debug.Log(waterComponents[0].anchoredPosition);
        }
        // reset?
        if (reset) {
            // wait
            yield return new WaitForSeconds(1);
            // reset
            yield return DecreaseWaterAnimation(waterComponents[1].anchoredPosition.y);
        }
        yield return new WaitForSeconds(2);
        ShowcaseTemplateController.Instance.OnEndOfUpdateWater();
    }

    IEnumerator DecreaseWaterAnimation(float aimingY)
    {
        while (waterComponents[0].anchoredPosition.y > aimingY)
        {
            yield return new WaitForEndOfFrame();
            waterComponents[0].anchoredPosition +=
                new Vector2(0, Time.deltaTime * resetAmountPerSec);
        }
    }
}
