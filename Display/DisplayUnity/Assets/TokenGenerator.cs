using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class TokenGenerator : MonoBehaviour
{
    [SerializeField] Rigidbody2D newToken;
    [SerializeField] Vector2 force;
    [SerializeField] Transform startPos;
    [SerializeField] Vector3 pos;

    [SerializeField] Rigidbody2D[] sampleTokens;
    [SerializeField] Vector2[] initialForce;
    [SerializeField] Transform generatedParent;

    void Start()
    {
        pos = startPos.position;
    }

    // Update is called once per frame
    void Update()
    {
        if (Input.GetKeyDown(KeyCode.A)) {
            newToken.AddForce(force, ForceMode2D.Impulse);
        }

        if (Input.GetKeyDown(KeyCode.R)) {
            newToken.gameObject.transform.position = pos;
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

    void GenerateNewToken(int idx) {
        GameObject token = Instantiate(sampleTokens[idx].gameObject, pos, new Quaternion(), generatedParent);
        newToken = token.GetComponent<Rigidbody2D>();
        newToken.AddForce(force, ForceMode2D.Impulse);
    }
}
