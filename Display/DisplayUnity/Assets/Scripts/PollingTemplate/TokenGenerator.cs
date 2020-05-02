using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class TokenGenerator : MonoBehaviour
{
    // test
    [SerializeField] Rigidbody2D newToken;
    // 
    [SerializeField] Vector2 force;
    [SerializeField] Transform startPos;
    [SerializeField] Rigidbody2D[] sampleTokens;
    [SerializeField] Transform generatedParent;
    [SerializeField] bool generateBigOnce = false;
    [SerializeField] int[] tokenOrder = { 2, 0, 1};
    [SerializeField] int totalTokens = 0;
    [SerializeField] int maxTokens = 10;
    [SerializeField] float resetFadingTime = 0.3f;

    void Start()
    {
    }

    // Update is called once per frame
    void Update()
    {
        if (Input.GetKeyDown(KeyCode.A)) {
            newToken.AddForce(force, ForceMode2D.Impulse);
        }

        if (Input.GetKeyDown(KeyCode.R)) {
            newToken.gameObject.transform.position = startPos.position;
        }

        if (Input.GetKeyDown(KeyCode.Z)) {
            GenerateNewToken(0);
        }

        if (Input.GetKeyDown(KeyCode.X))
        {
            GenerateNewToken(1);
        }

        if (Input.GetKeyDown(KeyCode.C))
        {
            GenerateNewToken(2);
        }
    }

    public void GenerateNewToken() {
        int orderIdx = 0;
        if (generateBigOnce && totalTokens == 0)
        {
            orderIdx = 0;
        }
        else if (generateBigOnce) {
            // only generate small and medium
            orderIdx = (totalTokens - 1) % (tokenOrder.Length - 1) + 1;
        }
        else
        {
            // generate in L, S, M
            orderIdx = totalTokens % tokenOrder.Length;
        }
        GenerateNewToken(tokenOrder[orderIdx]);
    }

    void GenerateNewToken(int idx) {
        GameObject token = Instantiate(sampleTokens[idx].gameObject, startPos.position, new Quaternion(), generatedParent);
        newToken = token.GetComponent<Rigidbody2D>();
        token.GetComponent<Rigidbody2D>().AddForce(force, ForceMode2D.Impulse);
        totalTokens++;
        if (totalTokens >= maxTokens) {
            StartCoroutine(ResetTokens());
        }
    }

    IEnumerator ResetTokens()
    {
        yield return new WaitForSeconds(1.5f);
        Token[] allTokens =
            generatedParent.GetComponentsInChildren<Token>();
        foreach (Token t in allTokens)
        {
            ParticleSystem p = t.particle;
            if (p) {
                p.Play();
            }
        }
        // fade out effect
        float fadeAmount = 1 / resetFadingTime;
        while (allTokens.Length > 0 && allTokens[0].filling.color.a > 0) {
            yield return new WaitForEndOfFrame();
            Color c = allTokens[0].filling.color;
            c.a -= fadeAmount * Time.deltaTime;
            foreach (Token t in allTokens)
            {
                t.filling.color = c;
            }
        }

        foreach (Token t in allTokens)
        {

            Destroy(t.gameObject);
        }
        totalTokens = 0;
    }
}
