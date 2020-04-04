using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class TouchPointController : MonoBehaviour
{
    #region Singleton
    public static TouchPointController Instance = null;

    private void Awake()
    {
        if (Instance == null)
        {
            Instance = this;
        }
    }
    #endregion

    [SerializeField] TouchPoint[] touchPoints;

    private void Start()
    {
        touchPoints = GetComponentsInChildren<TouchPoint>();
    }

    public void EnableAll() {
        foreach (TouchPoint tp in touchPoints)
        {
            tp.enabled = true;
        }
    }

    public void DisableAll() {
        foreach (TouchPoint tp in touchPoints)
        {
            tp.enabled = true;
        }
    }

    public void DisableExcept(int idx) {
        for (int i = 0; i < touchPoints.Length; ++i) {
            if (i == idx)
            {
                touchPoints[i].enabled = true;
            }
            else
            {
                touchPoints[i].enabled = false;
            }
        }
    }

    public void OnStartTouch(int id) {
        // touch starts on touch point
        // change state
        TextTemplateController.Instance.SetActiveOption(id);
        TextTemplateController.Instance.SetTemplateState(TextTemplateController.TemplateState.Loading);
    }

    public void OnAbortTouch(int id) {
        // touch aborted on touch point, back to idle 
        // change state
        TextTemplateController.Instance.SetTemplateState(TextTemplateController.TemplateState.Idle);
        TextTemplateController.Instance.SetActiveOption(-1);
    }

    public void OnEndTouch(int id)
    {
        // touch finished on touch point, scroll main bubble with answer
        // change state
        TextTemplateController.Instance.SetTemplateState(TextTemplateController.TemplateState.Scrolling);
    }
}
