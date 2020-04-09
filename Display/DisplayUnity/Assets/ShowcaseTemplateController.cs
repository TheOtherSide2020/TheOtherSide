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

                break;
            case TemplateState.Loading:

                break;
            case TemplateState.Scrolling:

                break;
            case TemplateState.Display:

                break;
        };
    }
}
