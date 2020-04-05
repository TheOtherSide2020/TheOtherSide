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
    [SerializeField] GameObject[] display;
    void Start()
    {
        display[0].SetActive(true);
    }

    public void OnStartPlaytest() {
        // start timer
        // hide instruction
        display[0].SetActive(false);
        startTime = (DateTime.Now);
    }

    public void LogEndTime() {
        endTime = (DateTime.Now);
    }

    public void LogFailAttempt() {
        failedAttempt++;
    }

    public void OnShowResult() {
        TimeSpan ts = endTime - startTime;
        // update text
        resultText[0].SetText(failedAttempt.ToString());
        resultText[1].SetText(ts.TotalSeconds.ToString());
        // show result
        display[1].SetActive(true);
        // write result in file
    }
}
