using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.IO;
using System;

public class ResultLoader : MonoBehaviour
{
    public static ResultLoader Instance = null;

    [Serializable]
    public class VoteCount
    {
        public string option;
        public int voteCount;
    }

    [Serializable]
    public class Result
    {
        public string firstPosted;
        public string lastUpdate;
        public int totalVote;   
        public string question;
        public VoteCount[] voteCounts;
    }

    Result pollingResult;
    [SerializeField] bool usingHardCode = false;
    [SerializeField] VoteCount[] testCounts;
    private void Awake()
    {
        if (Instance == null)
        {
            Instance = this;
        }
        if (usingHardCode)
        {
            pollingResult = new Result();
            pollingResult.voteCounts = testCounts;
        }
        else
        {
            using (StreamReader r = new StreamReader("playtestResult.json"))
            {
                string json = r.ReadToEnd();
                pollingResult = JsonUtility.FromJson<Result>(json);
            }
        }
        Debug.Log(pollingResult);
    }

    // called at beginning of the display
    public string GetOptionCount(int idx)
    {
        if (idx >= pollingResult.voteCounts.Length) return "Invalid";
        return pollingResult.voteCounts[idx].voteCount.ToString();
    }

    public void IncreaseVote(int idx) {
        SetOptionCount(idx, pollingResult.voteCounts[idx].voteCount + 1);
    }

    void SetOptionCount(int idx, int newCount)
    {
        if (idx >= pollingResult.voteCounts.Length) return;
        pollingResult.voteCounts[idx].voteCount = newCount;
    }

    private void OnDestroy()
    {
        // switching the template 
        // write result to file
    }
}

