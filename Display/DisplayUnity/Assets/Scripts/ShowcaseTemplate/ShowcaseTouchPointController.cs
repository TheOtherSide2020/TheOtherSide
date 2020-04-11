using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ShowcaseTouchPointController : MonoBehaviour
{
    #region Singleton
    public static ShowcaseTouchPointController Instance = null;

    private void Awake()
    {
        if (Instance == null)
        {
            Instance = this;
        }
    }
    #endregion

    [SerializeField] ShowcaseTouchPoint[] touchPoints;
    public float loadingTime = 1.5f;

    private void Start()
    {
        touchPoints = GetComponentsInChildren<ShowcaseTouchPoint>();
    }

    public void ResetAllProgress()
    {
        foreach (TouchPoint tp in touchPoints)
        {
            tp.ResetProgress();
        }
    }

    public void EnableAll()
    {
        foreach (TouchPoint tp in touchPoints)
        {
            tp.interactionEnabled = true;
        }
    }

    public void DisableAll()
    {
        foreach (TouchPoint tp in touchPoints)
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
        ShowcaseTemplateController.Instance.SetActiveOption(id);
        ShowcaseTemplateController.Instance.SetTemplateState(TemplateMainController.TemplateState.Loading);
    }

    public void OnAbortTouch(int id)
    {
        // playtest logging
        PlaytestController.Instance.LogFailAttempt();
        // touch aborted on touch point, back to idle 
        // change state
        ShowcaseTemplateController.Instance.SetTemplateState(TemplateMainController.TemplateState.Idle);
        ShowcaseTemplateController.Instance.SetActiveOption(-1);
    }

    public void OnEndTouch(int id)
    {
        // playtest logging
        PlaytestController.Instance.LogEndTime();
        // touch finished on touch point, scroll main bubble with answer
        // change state
        ShowcaseTemplateController.Instance.SetTemplateState(TemplateMainController.TemplateState.Reacting);
    }
}

