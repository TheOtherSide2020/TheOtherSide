using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PollingTouchPointController : MonoBehaviour
{
    #region Singleton
    public static PollingTouchPointController Instance = null;

    private void Awake()
    {
        if (Instance == null)
        {
            Instance = this;
        }
    }
    #endregion

    [SerializeField] PollingTouchPoint[] touchPoints;
    public float loadingTime = 1.5f;


    private void Start()
    {
        touchPoints = GetComponentsInChildren<PollingTouchPoint>();
        //LoadOptionText();
        //UpdateResultText();
    }

    public void LoadOptionText()
    {
        for (int i = 0; i < touchPoints.Length; ++i)
        {
            string optionText = PollingTemplateJsonLoader.Instance.GetOption(touchPoints[i].id);
            touchPoints[i].SetText(optionText);
            touchPoints[i].AdjustContainer();
        }
    }

    public void UpdateResultText() {
        for (int i = 0; i < touchPoints.Length; ++i)
        {
            string optionResultText = ResultLoader.Instance.GetOptionCount(touchPoints[i].id);
            touchPoints[i].SetResultText(optionResultText);
        }
    }

    public void ResetAllProgress()
    {
        foreach (PollingTouchPoint tp in touchPoints)
        {
            tp.ResetProgress();
        }
    }

    public void EnableAll()
    {
        foreach (PollingTouchPoint tp in touchPoints)
        {
            tp.interactionEnabled = true;
        }
    }

    public void DisableAll()
    {
        foreach (PollingTouchPoint tp in touchPoints)
        {
            tp.interactionEnabled = false;
        }
    }

    public void DisableExcept(int idx)
    {
        for (int i = 0; i < touchPoints.Length; ++i)
        {
            if (i == idx)
            {
                touchPoints[i].interactionEnabled = true;
            }
            else
            {
                touchPoints[i].interactionEnabled = false;
            }
        }
    }

    public void OnStartTouch(int id)
    {
        // touch starts on touch point
        // change state
        PollingTemplateController.Instance.SetActiveOption(id);
        PollingTemplateController.Instance.SetTemplateState(TemplateMainController.TemplateState.Loading);
    }

    public void OnAbortTouch(int id)
    {
        // playtest logging
        PlaytestController.Instance.LogFailAttempt();
        // touch aborted on touch point, back to idle 
        // change state
        PollingTemplateController.Instance.SetTemplateState(TemplateMainController.TemplateState.Idle);
        PollingTemplateController.Instance.SetActiveOption(-1);
    }

    public void OnEndTouch(int id)
    {
        // playtest logging
        PlaytestController.Instance.LogEndTime();
        // touch finished on touch point, scroll main bubble with answer
        // change state
        PollingTemplateController.Instance.SetTemplateState(TemplateMainController.TemplateState.Reacting);
    }
}

