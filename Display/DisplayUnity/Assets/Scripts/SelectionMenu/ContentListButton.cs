using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class ContentListButton : MonoBehaviour
{
    public int idx;
    public string title;
    public TMPro.TextMeshProUGUI text;
    public bool isActive = false;
    Button button;
    [SerializeField] SpriteRenderer activeDot;

    void Awake()
    {
        UpdateTitle();
        button = GetComponent<Button>();
        button.onClick.AddListener(() => OnClick(idx));
    }

    public void OnClick(int idx) {
        SelectionMenu.Instance.PreviewContent(idx, title) ;
    }

    public void UpdateTitle()
    {
        text.SetText(title);
    }

    public void SetActiveDisplayStatus(bool isActive) {
        activeDot.gameObject.SetActive(isActive);
    }
}
