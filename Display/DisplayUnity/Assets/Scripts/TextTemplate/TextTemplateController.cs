using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class TextTemplateController : MonoBehaviour
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

    public enum TemplateState
    {
        Idle,
        Loading,
        Scrolling,
        Display
    }

    public TemplateState templateState { get; private set; }

    // current active option that is being selected
    [SerializeField] int selectedId = -1;

    public void SetActiveOption(int id) {
        selectedId = id;
    }

    public void SetTemplateState(TemplateState state)
    {
        this.templateState = state;
        OnStateChange();
    }

    void OnStateChange() {
        switch (templateState) {
            case TemplateState.Idle:
                // enable all particle effects and touch point to accept input
                TouchPointController.Instance.EnableAll();
                TouchPointController.Instance.EnableEffects();
                TouchPointController.Instance.ResetAllProgress();
                MessageScroller.Instance.ResetIdleStatus();
                MessageScroller.Instance.StartTyping();
                break;
            case TemplateState.Loading:
                // disable all particle effects and touch point
                TouchPointController.Instance.DisableExcept(selectedId);
                TouchPointController.Instance.DisableEffects();
                break;
            case TemplateState.Scrolling:
                // disable interaction
                TouchPointController.Instance.DisableAll();
                // option bubble play check mark
                TouchPointController.Instance.PlayCheckMark(selectedId);
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

    private void Start()
    {
        SetTemplateState(TemplateState.Idle);
    }

    // Update is called once per frame
    void Update()
    {
        
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
        yield return new WaitForSeconds(1);
        TouchPointController.Instance.ResetCheckMark(selectedId);
        selectedId = -1;
        SetTemplateState(TemplateState.Idle);
        // for playtest logging
        yield return new WaitForSeconds(3);
        PlaytestController.Instance.OnShowResult();
    }
}
