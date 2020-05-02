using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class ShowcaseTouchPoint : TouchPoint
{
    [SerializeField] Animator dropAnimation;
    [SerializeField] int voteToFillBubble = 8;
    [SerializeField] WaterUpdater waterUpdater;
    [SerializeField] ArrowEffect arrowEffect;

    protected override void Start()
    {
        base.Start();
        dropAnimation.gameObject.SetActive(false);
    }

    //private void Update()
    //{
    //    if (Input.GetKeyDown(KeyCode.L)) {
    //        SetResultText("18 people selected this option");
    //    }
    //}

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

    public void SetArrowEffect(bool isActive) {
        arrowEffect.gameObject.SetActive(isActive);
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
        StartCoroutine(DisplayResultText(txt));
    }

    IEnumerator DisplayResultText(string txt) {
        string optionText = textDisplay.text;
        float changeAmount = 1 / ShowcaseTouchPointController.Instance.resultTextFadeTime;
        Color c = textDisplay.color;
        // option fade out
        while (textDisplay.color.a > 0) {
            yield return new WaitForEndOfFrame();
            c.a -= changeAmount * Time.deltaTime; 
            textDisplay.color = c;
        }
        SetText(txt);
        // result fade in
        while (textDisplay.color.a < 1)
        {
            yield return new WaitForEndOfFrame();
            c.a += changeAmount * Time.deltaTime;
            textDisplay.color = c;
        }
        // show result
        yield return new WaitForSeconds(2);
        // result fade out
        while (textDisplay.color.a > 0)
        {
            yield return new WaitForEndOfFrame();
            c.a -= changeAmount * Time.deltaTime;
            textDisplay.color = c;
        }
        SetText(optionText);
        // option fade in
        while (textDisplay.color.a < 1)
        {
            yield return new WaitForEndOfFrame();
            c.a += changeAmount * Time.deltaTime;
            textDisplay.color = c;
        }
        ShowcaseTemplateController.Instance.OnEndDisplayResultText();
    }
}
