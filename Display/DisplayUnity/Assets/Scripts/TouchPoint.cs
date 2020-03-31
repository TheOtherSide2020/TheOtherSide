using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class TouchPoint : MonoBehaviour
{
    [SerializeField] Image fillingImage;
    [SerializeField] float progress = 0f;
    public float loadingTime = 1.5f;

    // Start is called before the first frame update
    void Start()
    {
        fillingImage.fillAmount = 0;
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
        progress += amount;
        fillingImage.fillAmount = progress;
        if (progress >= 1f) {
            OnEndVoting();
            ResetProgress();
        }
    }

    void OnEndVoting() {

    }
}
