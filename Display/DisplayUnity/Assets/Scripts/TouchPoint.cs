using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class TouchPoint : MonoBehaviour
{
    [SerializeField] protected Image fillingImage;
    [SerializeField] protected float progress = 0f;
    [SerializeField] protected TMPro.TextMeshPro textDisplay;
    [SerializeField] protected ContainerSizeUpdater sizeUpdater;

    public int id;
    public bool interactionEnabled = true;

    // Start is called before the first frame update
    protected virtual void Start()
    {
        ResetProgress();
    }

    public void ResetProgress()
    {
        fillingImage.fillAmount = 0;
        progress = 0f;
    }

    virtual public void StopProgress() {
        if (!interactionEnabled) return;
        if (progress >= 1f)
        {
            return;
        }
        //TouchPointController.Instance.OnAbortTouch(id);
    }

    virtual public void IncreaseProgress(float amount) {
        if (!interactionEnabled) return;
        progress += amount;
        fillingImage.fillAmount = progress;
        if (progress >= 1f) {
            OnEndVoting();
        }
    }

    virtual protected void OnEndVoting() {
        TouchPointController.Instance.OnEndTouch(id);
    }

    public void SetText(string txt) {
        textDisplay.SetText(txt);
    }

    public void AdjustContainer()
    {
        sizeUpdater.UpdateSize();
    }
}
