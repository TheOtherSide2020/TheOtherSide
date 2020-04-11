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
                ShowcaseTouchPointController.Instance.ResetAllProgress();
                break;
            case TemplateState.Loading:
                // disable other touchpoints
                ShowcaseTouchPointController.Instance.DisableExcept(selectedId);
                break;
            case TemplateState.Reacting:

                break;
            case TemplateState.Display:

                break;
        };
    }
}
