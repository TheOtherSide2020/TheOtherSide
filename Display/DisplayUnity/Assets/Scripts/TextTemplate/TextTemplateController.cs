using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class TextTemplateController : TemplateMainController
{
    #region Singleton
    public static TextTemplateController Instance = null;

    private void Awake()
    {
        if (Instance == null)
        {
            Instance = this;
        }
    }
    #endregion

    protected override void OnStateChange() {
        Debug.Log("State change " + templateState);
        switch (templateState) {
            case TemplateState.Idle:
                // enable all particle effects and touch point to accept input
                TextTemplateTouchPointController.Instance.EnableAll();
                TextTemplateTouchPointController.Instance.EnableEffects();
                TextTemplateTouchPointController.Instance.ResetAllProgress();
                MessageScroller.Instance.ResetIdleStatus();
                MessageScroller.Instance.StartTyping();
                break;
            case TemplateState.Loading:
                // disable all particle effects and touch point
                TextTemplateTouchPointController.Instance.DisableExcept(selectedId);
                TextTemplateTouchPointController.Instance.DisableEffects();
                break;
            case TemplateState.Reacting:
                // disable interaction
                TextTemplateTouchPointController.Instance.DisableAll();
                // option bubble play check mark
                TextTemplateTouchPointController.Instance.PlayCheckMark(selectedId);
                // main bubble scroll up selected answer
                StartCoroutine(AnswerScrollUp());
                break;
            case TemplateState.Display:
                // main bubble scroll up with result
                StartCoroutine(ResultScrollUp());
                // wait for some time
                // scroll question back
                //MessageScroller.Instance.ScrollUp("Question");
                break;
        };
    }

    IEnumerator AnswerScrollUp() {
        yield return new WaitForSeconds(5);
        MessageScroller.Instance.UpdateText("Answer", selectedId);
        MessageScroller.Instance.ScrollUp("Answer");
        SetTemplateState(TemplateState.Display);
    }

    IEnumerator ResultScrollUp()
    {
        yield return new WaitForSeconds(3);
        MessageScroller.Instance.ScrollUp("Result");
        yield return new WaitForSeconds(3);
        MessageScroller.Instance.ScrollUp("Question");
        yield return new WaitForSeconds(2);
        TextTemplateTouchPointController.Instance.ResetCheckMark(selectedId);
        selectedId = -1;
        SetTemplateState(TemplateState.Idle);
        // for playtest logging
        yield return new WaitForSeconds(3);
        PlaytestController.Instance.OnShowResult();
        
    }
}
