using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class FadeIn : MonoBehaviour
{
    SpriteRenderer sr;
    [SerializeField] float fadeTime;
    void Start()
    {
        sr = GetComponent<SpriteRenderer>();
        Color cur = sr.color;
        sr.color = new Color(cur.r, cur.g, cur.b, 0);
    }

    // Update is called once per frame
    void Update()
    {
        if (Input.GetKeyDown(KeyCode.Space)) {
            StartCoroutine(FadeInEffect());
        }
    }

    IEnumerator FadeInEffect() {
        float amount = 1 / fadeTime;
        while (sr.color.a < 1) {
            yield return new WaitForEndOfFrame();
            Color cur = sr.color;
            sr.color = new Color(cur.r, cur.g, cur.b, cur.a + amount * Time.deltaTime);
        }
    }
}
