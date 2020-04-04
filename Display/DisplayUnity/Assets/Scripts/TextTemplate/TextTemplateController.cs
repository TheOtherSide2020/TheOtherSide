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
                break;
            case TemplateState.Loading:
                // disable all particle effects and touch point
                TouchPointController.Instance.DisableExcept(selectedId);
                break;
            case TemplateState.Scrolling:
                // main bubble scroll up with answer
                TouchPointController.Instance.DisableAll();
                break;
            case TemplateState.Display:
                // main bubble scroll up with result
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
}
