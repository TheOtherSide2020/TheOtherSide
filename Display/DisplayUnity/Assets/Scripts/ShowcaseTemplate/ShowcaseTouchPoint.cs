using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class ShowcaseTouchPoint : TouchPoint
{
    //[SerializeField] ContainerSizeUpdater sizeUpdater;
    [SerializeField] Animator dropAnimation;
    [SerializeField] int voteToFillBubble = 8;
    [SerializeField] TMPro.TMP_Text countText;
    [SerializeField] WaterUpdater waterUpdater;

    protected override void Start()
    {
        base.Start();
        dropAnimation.gameObject.SetActive(false);
    }

    public void InitializeWater() {
        waterUpdater.UpdateIncreaseAmount(voteToFillBubble);
    }

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
        if (!interactionEnabled) return;
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

    public void PlayDropAnimation() {
        dropAnimation.gameObject.SetActive(true);
        dropAnimation.SetTrigger("playDrop");
        // wait until finish and set state to result display
        StartCoroutine(WaitToNextState());
    }

    IEnumerator WaitToNextState() {
        yield return new WaitForSeconds(3);
        dropAnimation.gameObject.SetActive(false);
        ShowcaseTouchPointController.Instance.OnEndDroppingAnimation();
    }

    public void IncreaseWater(int votes) {
        waterUpdater.IncreaseWaterLevel(votes % voteToFillBubble == 0);
    }

    public void ResetWater()
    {
        // reset back to initial point
        waterUpdater.ResetWaterLevel();
    }

    public void SetWater(int votes)
    {
        // set water level according to votes
        waterUpdater.SetWaterLevel(votes % voteToFillBubble);
    }

    public void SetResultText(string txt) {
        countText.SetText(txt);
    }
}
