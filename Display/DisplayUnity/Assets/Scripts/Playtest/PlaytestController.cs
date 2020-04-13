using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class PlaytestController : MonoBehaviour
{
    #region Singleton
    public static PlaytestController Instance = null;

    private void Awake()
    {
        if (Instance == null)
        {
            Instance = this;
        }
    }
    #endregion

    [SerializeField] DateTime startTime, endTime;
    [SerializeField] int failedAttempt;
    [SerializeField] TMPro.TextMeshPro[] resultText;
    [SerializeField] GameObject[] displayVR;
    [SerializeField] GameObject[] buttons;
    [SerializeField] bool is2DTesting = true;
    [SerializeField] GameObject[] instruction2D;
    [SerializeField] ShowcaseMainBubble player;
    void Start()
    {
        StartVRInstruction();
        // 2D instruction
        Start2DInstruction();
    }

    void StartVRInstruction() {
        displayVR[0].SetActive(true);
        buttons[0].SetActive(false);
        StartCoroutine(ShowButtonDelay(0));
    }

    IEnumerator ShowButtonDelay(int idx) {
        yield return new WaitForSeconds(3);
        buttons[idx].SetActive(true);
    }

    public void OnTriggerNextButtonVR(int idx) {
        if (idx == 2)
        {
            OnStartPlaytest();
            return;
        }
        displayVR[idx].SetActive(false);
        displayVR[idx + 1].SetActive(true);
        buttons[idx+1].SetActive(false);
        StartCoroutine(ShowButtonDelay(idx+1));
    }

    public void OnStartPlaytest() {
        // start timer
        // hide instruction
        displayVR[2].SetActive(false);
        startTime = (DateTime.Now);
        is2DTesting = false;
        player.PlayVideo();
    }

    public void LogEndTime() {
        endTime = (DateTime.Now);
    }

    public void LogFailAttempt() {
        failedAttempt++;
    }

    public void OnShowResult() {
        // update text
        resultText[0].SetText(failedAttempt.ToString());
        if (is2DTesting)
        {
            resultText[1].SetText("N/A");
        }
        else {
            // show result
            TimeSpan ts = endTime - startTime;
            resultText[1].SetText(String.Format("{0:0.#}", ts.TotalSeconds));
            displayVR[displayVR.Length-1].SetActive(true);
        }
        // write result in file
    }

    public void Start2DInstruction() {
        instruction2D[0].SetActive(true);
        instruction2D[1].SetActive(false);
    }

    public void Next2DIntruction() {
        instruction2D[1].SetActive(true);
        instruction2D[0].SetActive(false);
    }

    public void Close2DIntruction() {
        instruction2D[0].SetActive(false);
        instruction2D[1].SetActive(false);
    }
}
