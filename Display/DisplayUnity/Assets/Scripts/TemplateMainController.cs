using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class TemplateMainController : MonoBehaviour
{
    public enum TemplateState
    {
        Idle,
        Loading,
        Scrolling,
        Display
    }

    public TemplateState templateState;

    // current active option that is being selected
    [SerializeField] int selectedId = -1;

    private void Start()
    {
        SetTemplateState(TemplateState.Idle);
    }

    public void SetActiveOption(int id)
    {
        selectedId = id;
    }

    public void SetTemplateState(TemplateState state)
    {
        this.templateState = state;
        OnStateChange();
    }

    protected virtual void OnStateChange()
    {
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
