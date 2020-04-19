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

        public VoteCount() {
            option = "";
            voteCount = 0;
        }
    }

    [Serializable]
    public class Result
    {
        public string name;
        public string type;
        public string firstPosted;
        public string lastUpdated;
        public string question;
        public int totalVote;
        public VoteCount[] voteCounts;

        public Result(string t) {
            type = t;
            totalVote = 0;
            voteCounts = new VoteCount[4];
            for (int i = 0; i < voteCounts.Length; ++i) {
                VoteCount vc = new VoteCount();
                voteCounts[i] = vc;
            }
        }
    }

    Result pollingResult;
    [SerializeField] string type;
    [SerializeField] bool usingHardCode = false;
    [SerializeField] VoteCount[] testCounts;
    [SerializeField] string path;
    private void Awake()
    {
        if (Instance == null)
        {
            Instance = this;
        }
        if (usingHardCode)
        {
            pollingResult = new Result(type);
            pollingResult.voteCounts = testCounts;
        }
        else
        {
            // check if result file exists
            pollingResult = new Result(type);
            path = SelectionMenu.Instance.GetCurrentResultPath();
            if (File.Exists(path))
            {
                using (StreamReader r = new StreamReader(path))
                {
                    string json = r.ReadToEnd();
                    pollingResult = JsonUtility.FromJson<Result>(json);
                }
            }
            else {
                // File.Create(SelectionMenu.Instance.GetCurrentResultPath());
                // initilize result
                pollingResult.firstPosted = DateTime.Now.ToString("yyyy-MM-ddTHH:mm:ssZ");
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

    public int GetRawOptionCount(int idx)
    {
        if (idx >= pollingResult.voteCounts.Length) return 0;
        return pollingResult.voteCounts[idx].voteCount;
    }

    public void IncreaseVote(int idx) {
        SetOptionCount(idx, pollingResult.voteCounts[idx].voteCount + 1);
    }

    void SetOptionCount(int idx, int newCount)
    {
        if (idx >= pollingResult.voteCounts.Length) return;
        pollingResult.voteCounts[idx].voteCount = newCount;
    }

    public void UpdateResultInfo(string name, string type, string question, string[] options) {
        pollingResult.name = name;
        pollingResult.type = type;
        pollingResult.question = question;
        for (int i = 0; i < pollingResult.voteCounts.Length; ++i)
        {
            pollingResult.voteCounts[i].option = options[i];
        }
    }

    private void OnDestroy()
    {
        // switching the template 
        // update options and question
        int count = 0;
        for (int i = 0; i < pollingResult.voteCounts.Length; ++i)
        {
            count += pollingResult.voteCounts[i].voteCount;
        }
        pollingResult.totalVote = count;
        pollingResult.lastUpdated = DateTime.Now.ToString("yyyy-MM-ddTHH:mm:ssZ");
        // write result to file
        string json = JsonUtility.ToJson(pollingResult);
        File.WriteAllText(path, json);
    }
}

