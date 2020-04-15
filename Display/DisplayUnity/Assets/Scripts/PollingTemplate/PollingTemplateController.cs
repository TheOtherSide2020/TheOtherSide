using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PollingTemplateController : TemplateMainController
{
    #region Singleton
    public static PollingTemplateController Instance = null;

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
                PollingTouchPointController.Instance.EnableAll();
                PollingTouchPointController.Instance.ResetAllProgress();
                break;
            case TemplateState.Loading:
                // disable other touchpoints
                PollingTouchPointController.Instance.DisableExcept(selectedId);
                break;
            case TemplateState.Reacting:
                // disable interaction
                PollingTouchPointController.Instance.DisableAll();
                break;
            case TemplateState.Display:
                // number change
                ResultLoader.Instance.IncreaseVote(selectedId);
                // update text
                PollingTouchPointController.Instance.UpdateResultText();
                break;
        };
    }
}
