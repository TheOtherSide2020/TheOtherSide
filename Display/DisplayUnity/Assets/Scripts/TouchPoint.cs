using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class TouchPoint : MonoBehaviour
{
    [SerializeField] Image fillingImage;
    [SerializeField] float progress = 0f;
    public float loadingTime = 1.5f;
    public int id;

    // Start is called before the first frame update
    void Start()
    {
        ResetProgress();
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    public void ResetProgress() {
        fillingImage.fillAmount = 0;
        progress = 0f;
    }

    public void IncreaseProgress(float amount) {
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
}
