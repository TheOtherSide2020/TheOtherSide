using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PollingMainBubble : MonoBehaviour
{
    #region Singleton
    public static PollingMainBubble Instance = null;

    private void Awake()
    {
        if (Instance == null)
        {
            Instance = this;
        }
    }
    #endregion

    [SerializeField] int activeIdx = -1;
    [SerializeField] SpriteRenderer[] lights;

    void Start()
    {
        lights = GetComponentsInChildren<SpriteRenderer>();
        foreach (SpriteRenderer sr in lights) {
            sr.gameObject.SetActive(false);
        }
        StartLightBlubEffect();
    }

    public void StartLightBlubEffect() {
        StartCoroutine(LightBlubEffect());
    }

    IEnumerator LightBlubEffect()
    {
        while (true)
        {
            for (int i = 0; i < lights.Length; ++i) {
                lights[i].gameObject.SetActive(true);
                yield return new WaitForSeconds(0.8f);
                lights[i].gameObject.SetActive(false);
                if (PollingTemplateController.Instance.templateState != TemplateMainController.TemplateState.Idle)
                {
                    break;
                }
            }
            if (PollingTemplateController.Instance.templateState != TemplateMainController.TemplateState.Idle)
            {
                break;
            }
            yield return new WaitForSeconds(0.8f);
            for (int i = lights.Length - 1; i >= 0; --i)
            {
                lights[i].gameObject.SetActive(true);
                yield return new WaitForSeconds(0.8f);
                lights[i].gameObject.SetActive(false);
                if (PollingTemplateController.Instance.templateState != TemplateMainController.TemplateState.Idle)
                {
                    break;
                }
            }
            if (PollingTemplateController.Instance.templateState != TemplateMainController.TemplateState.Idle)
            {
                break;
            }
            yield return new WaitForSeconds(0.8f);
        }
    }

    //IEnumerator LightBlubEffect() {
    //    while (true) {
    //        int idx = Random.Range(0, lights.Length);
    //        if (idx == activeIdx)
    //        {
    //            idx = (idx + 1) % lights.Length;
    //        }
    //        if (activeIdx >= 0) {
    //            lights[activeIdx].gameObject.SetActive(false);
    //        }
    //        lights[idx].gameObject.SetActive(true);
    //        activeIdx = idx;
    //        yield return new WaitForSeconds(0.5f);
    //        if (PollingTemplateController.Instance.templateState != TemplateMainController.TemplateState.Idle) {
    //            lights[activeIdx].gameObject.SetActive(false);
    //            break;
    //        }
    //    }
    //}
}
