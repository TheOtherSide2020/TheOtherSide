using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ShowcaseTemplateController : TemplateMainController
{
    #region Singleton
    public static ShowcaseTemplateController Instance = null;

    private void Awake()
    {
        if (Instance == null)
        {
            Instance = this;
        }
    }
    #endregion

    protected override void OnStateChange() {
        switch (templateState)
        {
            case TemplateState.Idle:
                // enable all touchpoints
                ShowcaseTouchPointController.Instance.EnableAll();
                ShowcaseTouchPointController.Instance.EnableArrowEffect();
                ShowcaseTouchPointController.Instance.ResetAllProgress();
                break;
            case TemplateState.Loading:
                // disable other touchpoints
                ShowcaseTouchPointController.Instance.DisableExcept(selectedId);
                ShowcaseTouchPointController.Instance.DisableArrowEffect();
                break;
            case TemplateState.Reacting:
                // disable interaction
                ShowcaseTouchPointController.Instance.DisableAll();
                // play drop animation
                ShowcaseTouchPointController.Instance.PlayDropAnimation(selectedId);
                break;
            case TemplateState.Display:
                // number change
                ResultLoader.Instance.IncreaseVote(selectedId);
                // water increase
                ShowcaseTouchPointController.Instance.IncreaseWater(selectedId);
                break;
        };
    }

    public void OnEndOfUpdateWater() {
        // update text
        ShowcaseTouchPointController.Instance.ShowResultText(selectedId);
    }

    public void OnEndDisplayResultText()
    {
        selectedId = -1;
        SetTemplateState(TemplateState.Idle);
        // playtest: show end result
        // PlaytestController.Instance.OnShowResult();
    }
}
