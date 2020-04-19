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
                PollingMainBubble.Instance.StartLightBlubEffect();
                break;
            case TemplateState.Loading:
                // disable other touchpoints
                PollingTouchPointController.Instance.DisableExcept(selectedId);
                break;
            case TemplateState.Reacting:
                // disable interaction
                PollingTouchPointController.Instance.DisableAll();
                // generate and throw token
                TokenController.Instance.GenerateToken(selectedId);
                // wait for next state
                StartCoroutine(WaitForNextState(TemplateState.Display));
                break;
            case TemplateState.Display:
                // number change
                ResultLoader.Instance.IncreaseVote(selectedId);
                // update text
                PollingTouchPointController.Instance.UpdateResultText();
                // wait for next state
                selectedId = -1;
                StartCoroutine(WaitForNextState(TemplateState.Idle));
                break;
        };
    }

    IEnumerator WaitForNextState(TemplateState state) {
        yield return new WaitForSeconds(2);
        SetTemplateState(state);
    }
}
