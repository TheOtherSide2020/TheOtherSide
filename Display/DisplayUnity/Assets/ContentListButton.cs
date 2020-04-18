using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class ContentListButton : MonoBehaviour
{
    public int idx;
    public string title;
    public TMPro.TextMeshProUGUI text;
    Button button;

    void Awake()
    {
        text = GetComponentInChildren<TMPro.TextMeshProUGUI>();
        button = GetComponent<Button>();
        button.onClick.AddListener(() => OnClick(idx));
    }

    public void OnClick(int idx) {
        SelectionMenu.Instance.PreviewContent(idx);
    }

    public void OnEnable()
    {
        text.SetText(title);
    }
}
