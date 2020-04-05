using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class TouchPoint : MonoBehaviour
{
    [SerializeField] Image fillingImage;
    [SerializeField] Image checkMarkImage;
    [SerializeField] float progress = 0f;
    [SerializeField] TMPro.TextMeshPro textDisplay;
    [SerializeField] ContainerSizeUpdater sizeUpdater;

    public int id;
    public bool interactionEnabled = true;

    // Start is called before the first frame update
    void Start()
    {
        ResetProgress();
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    public void ResetProgress()
    {
        fillingImage.fillAmount = 0;
        progress = 0f;
    }

    public void StopProgress() {
        if (!interactionEnabled) return;
        if (progress >= 1f)
        {
            return;
        }
        TouchPointController.Instance.OnAbortTouch(id);
    }

    public void IncreaseProgress(float amount) {
        if (!interactionEnabled) return;
        if (progress == 0f) {
            TouchPointController.Instance.OnStartTouch(id);
        }
        progress += amount;
        fillingImage.fillAmount = progress;
        if (progress >= 1f) {
            OnEndVoting();
        }
    }

    void OnEndVoting() {
        TouchPointController.Instance.OnEndTouch(id);
    }

    public void SetText(string txt) {
        textDisplay.SetText(txt);
    }

    public void AdjustContainer() {
        sizeUpdater.UpdateSize();
    }

    public void ResetCheckMark()
    {
        textDisplay.gameObject.SetActive(true);
        checkMarkImage.fillAmount = 0f;
    }

    public void ShowCheckMark() {
        textDisplay.gameObject.SetActive(false);
        StartCoroutine(FillCheckMark(TouchPointController.Instance.checkMarkFillingTime));
    }

    IEnumerator FillCheckMark(float finishTimeInSec) {
        while (checkMarkImage.fillAmount < 1f) {
            checkMarkImage.fillAmount += Time.deltaTime / finishTimeInSec;
            yield return new WaitForEndOfFrame();
        }
    }
}
