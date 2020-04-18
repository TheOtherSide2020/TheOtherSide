using System.Collections;
using System.Collections.Generic;
using TMPro;
using UnityEngine;

public class MessageScroller : MonoBehaviour
{
    #region Singleton
    public static MessageScroller Instance = null;

    private void Awake()
    {
        if (Instance == null)
        {
            Instance = this;
        }
    }
    #endregion

    [SerializeField] List<GameObject> DisplayMsg;
    [SerializeField] List<GameObject> DisplayAnchor;
    [SerializeField] GameObject question;
    [SerializeField] GameObject answer;
    [SerializeField] GameObject result;
    [SerializeField] float scrollTime;
    [SerializeField] bool testScroll = false;
    [SerializeField] string testScrollStep = "Answer";

    enum ScrollingState {
        Scrolling,
        Idle
    }

    void Start()
    {
        ResetIdleStatus();
        // update question text
        UpdateText("Question");
    }

    private void Update()
    {
        if (testScroll) {
            ScrollUp(testScrollStep);
        }
    }

    public void ResetIdleStatus() {
        question.SetActive(true);
        answer.SetActive(false);
        result.SetActive(false);
    }

    public void UpdateText(string type, int idx = -1) {
        string newText = "";
        switch (type)
        {
            case "Question":
                newText = TextTemplateJsonLoader.Instance.GetQuestion();
                question.GetComponent<MainBubbleSingleMessage>().SetText(newText);
                question.GetComponent<ContainerSizeUpdater>().UpdateSize();
                break;
            case "Answer":
                // update answer text
                newText = TextTemplateJsonLoader.Instance.GetOption(idx);
                answer.GetComponent<MainBubbleSingleMessage>().SetText(newText);
                answer.GetComponent<ContainerSizeUpdater>().UpdateSize();
                break;
            case "Result":
                newText = "";
                result.GetComponent<MainBubbleSingleMessage>().SetText(newText);
                result.GetComponent<ContainerSizeUpdater>().UpdateSize();
                break;
        }
    }

    public void ScrollUp(string option) {
        switch (option) {
            case "Question":
                DisplayMsg[2] = question;
                break;
            case "Answer":
                // set text
                DisplayMsg[2] = answer;
                break;
            case "Result":
                // set text
                DisplayMsg[2] = result;
                break;
        }
        RectTransform curRec = DisplayMsg[2].GetComponent<RectTransform>();
        RectTransform targetRec = DisplayAnchor[2].GetComponent<RectTransform>();
        curRec.localScale = targetRec.localScale;
        curRec.position = targetRec.position;
        curRec.gameObject.SetActive(true);
        AudioPlayer.Instance.PlaySent();
        StartCoroutine(ScrollUpBubble());
    }
    IEnumerator ScrollUpBubble() {
        testScroll = false;
        if (DisplayMsg[0])
        {
            DisplayMsg[0].SetActive(false);
        }

        RectTransform upcomingRec = DisplayAnchor[2].GetComponent<RectTransform>();
        RectTransform curRec = DisplayAnchor[1].GetComponent<RectTransform>();
        RectTransform prevRec = DisplayAnchor[0].GetComponent<RectTransform>();

        RectTransform upcomingMovingRec = DisplayMsg[2].GetComponent<RectTransform>();
        float upcomingScaleChange = (curRec.localScale.x - upcomingMovingRec.localScale.x) / scrollTime;
        float upcomingposYChange = (curRec.position.y - upcomingMovingRec.position.y) / scrollTime;

        RectTransform curMovingRec = DisplayMsg[1].GetComponent<RectTransform>();
        float currentScaleChange = (prevRec.localScale.x - curRec.localScale.x) / scrollTime;
        float currentPosYChange = (prevRec.position.y - curRec.position.y) / scrollTime;
        while (upcomingMovingRec.localScale.x < curRec.localScale.x) {
            yield return new WaitForEndOfFrame();
            // move upcoming to current
            // update scale
            upcomingMovingRec.localScale += upcomingScaleChange * Time.deltaTime * Vector3.one;
            // update position
            upcomingMovingRec.position += new Vector3(0, upcomingposYChange * Time.deltaTime, 0);

            // move current to previous
            // update scale
            curMovingRec.localScale += currentScaleChange * Time.deltaTime * Vector3.one;
            // update position
            curMovingRec.position += new Vector3(0, currentPosYChange * Time.deltaTime, 0);
        }
        // update new display order
        DisplayMsg[0] = DisplayMsg[1];
        DisplayMsg[1] = DisplayMsg[2];
        DisplayMsg[2] = null;
    }

    public void StartTyping() {
        StartCoroutine(TypingEffect(question));
    }

    // question typing effect
    IEnumerator TypingEffect(GameObject mainBubbleComponent)
    {
        TMP_Text textComponent = mainBubbleComponent.GetComponentInChildren<TMP_Text>();
        textComponent.ForceMeshUpdate();
        TMP_TextInfo textInfo = textComponent.textInfo;

        int totalVisibleCharacters = textInfo.characterCount; // Get # of Visible Character in text object
        int visibleCount = 0;
        while (
            TextTemplateController.Instance.templateState == TextTemplateController.TemplateState.Idle ||
            (TextTemplateController.Instance.templateState != TextTemplateController.TemplateState.Idle &&
                visibleCount <= totalVisibleCharacters)
            )
        {
            if (visibleCount > totalVisibleCharacters)
            {
                yield return new WaitForSeconds(3.0f);
                if (TextTemplateController.Instance.templateState == TextTemplateController.TemplateState.Idle)
                    visibleCount = 0;
            }
            textComponent.maxVisibleCharacters = visibleCount; // How many characters should TextMeshPro display?
            visibleCount += 1;
            yield return new WaitForSeconds(0.05f);
        }
    }
}
