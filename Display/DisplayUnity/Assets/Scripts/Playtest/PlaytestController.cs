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
    [SerializeField] bool is2DTesting = true;

    void Start()
    {
        display[0].SetActive(true);
    }

    public void OnStartPlaytest() {
        // start timer
        // hide instruction
        display[0].SetActive(false);
        startTime = (DateTime.Now);
        is2DTesting = false;
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
            display[1].SetActive(true);
        }
        // write result in file
    }
}
