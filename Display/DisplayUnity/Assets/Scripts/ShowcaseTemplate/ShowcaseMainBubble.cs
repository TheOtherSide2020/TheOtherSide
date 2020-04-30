using System.Collections;
using System.Collections.Generic;
using TMPro;
using UnityEngine;
using UnityEngine.Video;

public class ShowcaseMainBubble : MonoBehaviour
{
    [SerializeField] VideoPlayer player;
    [SerializeField] SpriteRenderer poster;
    [SerializeField] float initialPosterAlpha;
    [SerializeField] float showTextTime = 0.5f;
    [SerializeField] float questionShowTime = 5f;
    [SerializeField] float pictureShowTime = 5f;
    [SerializeField] TMP_Text question;
    [SerializeField] bool pictureOnly = false;

    void Start()
    {
        // update questions
        question = GetComponentInChildren<TMP_Text>();
        question.SetText(ShowcaseTemplateJsonLoader.Instance.GetQuestion());
        SetQuestionAlpha(0);
        initialPosterAlpha = poster.color.a;
        // set picture
        Sprite pic = ShowcaseTemplateJsonLoader.Instance.GetPicture();
        // update poster
        poster.sprite = pic;

        // set video
        player = GetComponentInChildren<VideoPlayer>();
        player.loopPointReached += OnEndOfVideo;
        string videoUrl = ShowcaseTemplateJsonLoader.Instance.GetVideoUrl();
        if (pictureOnly || videoUrl == "")
        {
            SetPosterAlpha(1);
            StartCoroutine(PosterOnlyProcess());
            player.gameObject.SetActive(false);
        }
        else {
            player.url = videoUrl;
            player.Play();
        }
    }

    public void PlayVideo() {
        player.gameObject.SetActive(true);
        player.Play();
    }

    void OnEndOfVideo(VideoPlayer vp) {
        player.gameObject.SetActive(false);
        // show text
        StartCoroutine(AfterVideoProcess());
    }

    IEnumerator PosterOnlyProcess() {
        while (true) {
            yield return new WaitForSeconds(pictureShowTime);
            // hide poster, show question
            while (question.color.a < 1)
            {
                yield return new WaitForEndOfFrame();
                float newAlpha = question.color.a +
                    Time.deltaTime / showTextTime;
                SetQuestionAlpha(newAlpha);
                newAlpha = poster.color.a -
                Time.deltaTime * ((1 - initialPosterAlpha) / showTextTime);
                SetPosterAlpha(newAlpha);
                Debug.Log(newAlpha);
            }
            yield return new WaitForSeconds(questionShowTime);
            // show poster, hide question
            while (question.color.a > 0)
            {
                yield return new WaitForEndOfFrame();
                float newAlpha = question.color.a -
                    Time.deltaTime / showTextTime;
                SetQuestionAlpha(newAlpha);
                newAlpha = poster.color.a +
                Time.deltaTime * ((1 - initialPosterAlpha) / showTextTime);
                SetPosterAlpha(newAlpha);
            }
        }
    }

    IEnumerator AfterVideoProcess() {
        while (question.color.a < 1) {
            yield return new WaitForEndOfFrame();
            float newAlpha = question.color.a + 
                Time.deltaTime / showTextTime;
            SetQuestionAlpha(newAlpha);
        }
        yield return new WaitForSeconds(questionShowTime);
        player.gameObject.SetActive(true);
        player.Play();
        SetQuestionAlpha(0);
    }

    void SetQuestionAlpha(float a) {
        question.color = new Color(
            question.color.r, question.color.g, 
            question.color.b, a);
    }

    void SetPosterAlpha(float a) {
        poster.color = new Color(
            poster.color.r, poster.color.g,
            poster.color.b, a);
    }
}